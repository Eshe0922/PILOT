import torch.nn as nn
import torch
import copy
from pytorch_metric_learning import losses

loss_func = losses.NTXentLoss(temperature=0.1)
loss_func1 = losses.SupConLoss(temperature = 0.1)
import torch.nn.functional as F
class Model(nn.Module):   
    def __init__(self, encoder,config,tokenizer,args):
        super(Model, self).__init__()
        self.encoder = encoder
        self.config=config
        self.tokenizer=tokenizer
        self.args=args
        self.fc = nn.Linear(1*768, 1)
        
    def forward(self, input_ids=None,labels=None,epochs_now = None,epoch_max = None,type = None): 
        outputs=self.encoder(input_ids,attention_mask=input_ids.ne(1),
                                output_hidden_states=True, return_dict=True)
        
        cls_first = outputs.hidden_states[1][:,0,:]
        cls_last = outputs.hidden_states[-1][:,0,:]

        cls = cls_first + cls_last
        cls = cls.squeeze()
        logits=self.fc(cls)
        prob=torch.sigmoid(logits)
        prob = prob.reshape(prob.shape[0],-1)

        if labels is not None:
            labels=labels.float()
            loss=torch.log(prob[:,0]+1e-10)*labels+torch.log((1-prob)[:,0]+1e-10)*(1-labels)
            if type == 'do_train_iterative':
                weight = 1-(epochs_now/(epoch_max+1))**1
                loss = loss*weight
            loss=-loss.mean()
            return loss, prob, cls
        else:
            return prob, cls
        
class Model_train_3(nn.Module):   
    def __init__(self, encoder,config,tokenizer,args):
        super(Model_train_3, self).__init__()
        self.encoder = encoder
        self.config=config
        self.tokenizer=tokenizer
        self.args=args
        self.fc = nn.Linear(1*768, 1)
        self.con_para = nn.Parameter(torch.ones(1)*0.5).cuda()
        
    def forward(self, input_ids=None,labels=None,epochs_now = None,epoch_max = None,type = None): 
        outputs=self.encoder(input_ids,attention_mask=input_ids.ne(1),
                                output_hidden_states=True, return_dict=True)
        
        cls_first = outputs.hidden_states[1][:,0,:]
        cls_last = outputs.hidden_states[-1][:,0,:]
        cls = cls_first + cls_last
        logits =self.fc(cls)
        prob=torch.sigmoid(logits)
        prob = prob.reshape(prob.shape[0],-1)

        if labels is not None:
            labels=labels.float()
            loss= loss_func(cls, labels)
            loss1= loss_func1(cls, labels)
            loss_cr = torch.log(prob[:,0]+1e-10)*labels+torch.log((1-prob)[:,0]+1e-10)*(1-labels)
            loss = (1 - self.con_para) * loss.mean()+ self.con_para * loss1.mean() - loss_cr.mean()
            return loss, prob, cls
        else:
            return prob, cls

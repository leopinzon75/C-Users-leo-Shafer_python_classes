 

class Router:
     '''Router Class'''
     def __init__(self, model, swversion, ip_add): 
        '''Initialize values'''
        self.model = model
        self.swversion =swversion
        self.ip_add = ip_add
 

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr1.desc = 'virtual router'
print(rtr1.desc)    
    
rtr2= Router('isr4221', '16.9.5', '10.10.10.5')
print(rtr2.model)

  
      
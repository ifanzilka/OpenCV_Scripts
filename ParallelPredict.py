from threading import Thread

def fun_model(model,res, method, *argv):
    
    if method=='__call__':
        res[0] = model(*argv)
    else:
        exec("res[0] = model." + method + "(*argv)")
    #res[0] = model(frame)
    return 0 

class ParallelThreadPredict:
    """
    class for parallel Predictor
    """
    
    def __init__(self, lst_model, default_return = None):
        """
        lst_model = [Fom512(cuda:0), Fom512(cuda:1)]
        """
        self.num_gpu = len(lst_model)
        self.lst_model = lst_model
        
        # list class Predictor witch other device
        
        ## Param  ##
        self.num_frame = 0
        self.lst_res = [[1] for i in range(self.num_gpu)]
        self.lst_th  = [ None for i in range(self.num_gpu)]
        
        self.default_return = default_return 
    def __call__(self, method, *argv):
        # methods is a call method in predict model
        # *argv arguments in predict model 
        
        if self.num_frame == 0:
            
            self.lst_th[0] = Thread(target=fun_model, args=(self.lst_model[0],self.lst_res[0], method,  *argv))
            self.lst_th[0].start()
            self.num_frame += 1
            return self.default_return
        
        else:
                
            num_gpu = self.num_frame % self.num_gpu
            pred = (num_gpu - 1) if (num_gpu - 1 > 0) else self.num_gpu - 1
                
            self.lst_th[num_gpu] = Thread(target=fun_model, args=(self.lst_model[num_gpu], self.lst_res[num_gpu], method,  *argv))
            self.lst_th[num_gpu].start()
                
            self.lst_th[pred].join()
            res = self.lst_res[pred][0]
            self.num_frame += 1
            
        return res

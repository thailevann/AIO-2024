#caculate MAE, MSE, RMSE loss function
import random
import math
def MAE(y_true, y_predict):
    return abs(y_predict-y_true)
def MSE( y_true, y_predict):
    return (y_true-y_predict)**2
if __name__== "__main__":

    print("Input number of sample (integer number) which are generated: ")
    n_sample = input()
    if n_sample.isnumeric() == False:
        print("number of sampes must be an integer number")
    else:
        predict_list = []
        target_list = []
        loss_list = []
        loss_name_list = ["RMSE", "MSE", "MAE"]
        print("Input loss name: ")
        loss_name = input()
        if loss_name not in loss_name_list:
            print(f'{loss_name} is not supported')
        else:
            for i in range(0, int(n_sample)):
                predict = random.uniform(0,10)
                target = random.uniform(0,10)
                if loss_name == "RMSE" or loss_name =="MSE":
                    loss = MSE(target, predict)
                if loss_name == "MAE":
                    loss = MAE(target, predict)
                print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}")
                print(f'loss: {loss}')
                loss_list.append(loss)
            final_loss = sum(loss_list)/int(n_sample)
            if loss_name == 'RMSE':
                final_loss = math.sqrt(final_loss)
            print(f"final {loss_name}: {final_loss}")

    

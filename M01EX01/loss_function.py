# Calculate MAE, MSE, RMSE loss functions
import random
import math

def mae(y_true, y_predict):
    return abs(y_predict - y_true)

def mse(y_true, y_predict):
    return (y_true - y_predict) ** 2

if __name__ == "__main__":
    n_sample = input("Input number of samples (integer number) to be generated: ")

    if not n_sample.isnumeric():
        print("Number of samples must be an integer.")
    else:
        n_sample = int(n_sample)
        loss_list = []
        loss_name_list = ["RMSE", "MSE", "MAE"]

        loss_name = input("Input loss name (RMSE | MSE | MAE): ").strip().upper()
        
        if loss_name not in loss_name_list:
            print(f'{loss_name} is not supported')
        else:
            for i in range(n_sample):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                
                if loss_name in ["RMSE", "MSE"]:
                    loss = mse(target, predict)
                elif loss_name == "MAE":
                    loss = mae(target, predict)
                
                print(f"Loss name: {loss_name}, Sample: {i}, Pred: {predict:.2f}, Target: {target:.2f}")
                print(f'Loss: {loss:.4f}')
                loss_list.append(loss)
            
            final_loss = sum(loss_list) / n_sample
            
            if loss_name == 'RMSE':
                final_loss = math.sqrt(final_loss)
            
            print(f"Final {loss_name}: {final_loss:.4f}")

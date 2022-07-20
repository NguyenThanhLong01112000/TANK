import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]
#arg1 = "13_14_15_16_17_18_19_142_142_142_142_142_142_3_3_3_3_3_3_"
print("LSTM neuron network is running ...")
with open(arg2 + "Content/most_recent_item.txt", "w") as f:
    f.write(arg1)
s = arg1.split("_")
s = s[0:-1]
list_item = []
for item_id in s:
    list_item.append(int(item_id))
print("list_item_input = ", list_item)

if len(list_item) == 19:
    import torch
    import torch.nn as nn

    batch_size = 10
    embedding_dim = 64
    hidden_dim = 128
    item_number = 256
    class LSTMRating(nn.Module):
        def __init__(self, embedding_dim, hidden_dim, num_items):
            super().__init__()
            self.hidden_dim = hidden_dim
            self.item_embeddings = nn.Linear(1, embedding_dim)
            self.lstm = nn.LSTM(embedding_dim, hidden_dim)
            self.linear = nn.Linear(hidden_dim, num_items)
        def forward(self, input):
            input = input.view(batch_size, 19, 1)
            input = input.permute(1, 0, 2)
            embeddings = self.item_embeddings(input) 
            output, self.hidden = self.lstm(embeddings)
            ht = self.hidden[0]
            pred = self.linear(ht.permute(1, 0, 2))
            return pred
        
    model_load = LSTMRating(embedding_dim, hidden_dim, item_number)
    model_load.load_state_dict(torch.load(arg2 + "Content/best_model_state_dict.txt"))
    model_load.eval()

    list_item = torch.Tensor(list_item)

    item_rec = []
    model_load.eval()
    with torch.no_grad():
        embedding = model_load.item_embeddings(list_item.view(-1,1))
        output, hidden = model_load.lstm(embedding)
        one_host_pred = model_load.linear(hidden[0])
        one_host_list = list(one_host_pred.view(-1).detach().numpy())
        one_host_list_sorted = sorted(one_host_list, reverse = True)
        one_host_list_sorted = one_host_list_sorted[0:10]
        for i in range(0,10):
            item = one_host_list.index(one_host_list_sorted[i])
            item_rec.append(item)
        print("item_rec = ", item_rec)

    with open(arg2 + "Content/item_rec.txt", "w") as f:
        f.write("{}".format(item_rec))
else:
    print("list_item is not valid, must to have 19 element!!!")
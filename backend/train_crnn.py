# backend/train_crnn.py (simplified)
model = CRNN()
criterion = nn.CTCLoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(epochs):
    for imgs, labels in train_loader:
        output = model(imgs)
        loss = criterion(output, labels, ...)
        loss.backward()
        optimizer.step()


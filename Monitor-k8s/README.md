

- Deploy
```
kubectl create -f prometheus/
kubectl create -f grafana/
```

- Check SVC nodeport
```
kubectl get svc -n edge-monitoring 
```


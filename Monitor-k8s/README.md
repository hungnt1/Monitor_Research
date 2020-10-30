
- Khoi tao secret cho grafana
```
kubectl create secret generic grafana -n edge-monitoring \
    --from-literal=grafana-admin-password=admin \
    --from-literal=grafana-admin-user=admin 
```

- Deploy
```
kubectl create -f prometheus/
kubectl create secret generic grafana -n edge-monitoring \
    --from-literal=grafana-admin-password=admin \
    --from-literal=grafana-admin-user=admin 
kubectl create -f grafana/
```

- Khoi tao secret cho grafana
```

```

- Check SVC nodeport
```
kubectl get svc -n edge-monitoring 
```


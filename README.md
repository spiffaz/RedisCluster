# Redis Cluster on Kubernetes

This repository contains Kubernetes configuration files to deploy a Redis cluster using Kubernetes. The setup includes a ConfigMap for Redis configuration, a headless Service for DNS-based service discovery, a StatefulSet for managing Redis replicas, and PersistentVolumeClaims (PVCs) for data storage. 

## Prerequisites

Before deploying the Redis cluster, ensure you have the following prerequisites installed:

- [Kubernetes](https://kubernetes.io/) cluster up and running.
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) command-line tool configured to access your cluster.

## Configuration

The Redis cluster is configured using a ConfigMap named `redis-config`. The `redis.conf` file in this ConfigMap contains the Redis server configuration. You can customize this file to suit your requirements. Here's the default configuration:

```conf
bind 0.0.0.0
port 6379
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
# requirepass YOUR_REDIS_PASSWORD
```

## Deployment

To deploy the Redis cluster, follow these steps:

1. Apply the ConfigMap containing the Redis configuration:

```bash
kubectl apply -f redis-config.yaml
```

2. Create the headless Service for Redis:

```bash
kubectl apply -f redis-cluster-service.yaml
```

3. Deploy the StatefulSet for Redis replicas:

```bash
kubectl apply -f redis-cluster-statefulset.yaml
```

## Dockerfile

The Dockerfile provided in this repository extends the official Redis image. It copies the custom `redis.conf` file into the image and uses it as the configuration for the Redis server. You can build and push this Docker image to your container registry if needed.

## Scaling

You can scale the number of Redis replicas by updating the `replicas` field in the `redis-cluster-statefulset.yaml` file and then applying the changes:

```bash
kubectl apply -f redis-cluster-statefulset.yaml
```

## Data Persistence

Data persistence is ensured by using PersistentVolumeClaims (PVCs). Each Redis replica has its own PVC named `redis-data` with a default requested storage size of 30MiB. You can modify the storage size in the `redis-cluster-statefulset.yaml` file to meet your storage requirements.

## Accessing Redis

To access the Redis cluster, you can use the headless Service `redis-cluster-service` with DNS-based discovery. For example, to connect to the first Redis pod:

```bash
redis-cli -h redis-cluster-0.redis-cluster-service
```

## Maintenance

To update the Redis configuration, modify the `redis.conf` file in the `redis-config.yaml` ConfigMap. Changes will take effect upon restarting the Redis pods. You can perform rolling restarts by deleting and recreating pods or using Kubernetes rolling updates.

Feel free to customize this setup according to your specific needs and requirements.

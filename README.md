# RedisCluster
This creates a Redis cluster on Kubernetes

This includes a ConfigMap, a service, a statefulset and volumes for each statefulset.

The redis configuration is stored in the configmap. The configmap is mounted inside the containers as a volume.

This allows us to manage the configuration outside the container. The changes would take effect when the container or rollout is restarted.
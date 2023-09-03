This creates a sample python application to log to Redis. This can be used to test the Redis cluster to validate that the cluster works.

If running this locally with Docker. Save the log_to_redis.py script and the Dockerfile in the same directory, then build the dockerfile.

If you are running this with Kubernetes, apply the PythonApp.yaml file to your preferred namespace in your cluster.
The file would create a configmap with the script. The configmap would be attached as a volume and the command would be run when the container starts.
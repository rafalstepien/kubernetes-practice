# Notes

## How is kubernetes cluster built:
<img src=./cluster_schema.png width=400>

- A cluster consists of:
    - control plane (master), usually 3-5 control planes are deployed for high availability
    - worker nodes
    - DNS system (nodes within k8s can talk with each other thanks to DNS, every pod has hardcoded DNS address)
- Bascically in cluster, anyone can talk to anyone
- Worker nodes = kubelet + container runtime => heavy lifting: running apps, scripts
- Control plane node hosts:
    - /etcd database to store the desired state of the application
    - API, used by `kubectl` (this is the main frontend of the cluster)
    - Controller, that implements loops to control whether the current state of the cluster is consistent with desired state
    - Scheduler, that decides on which worker node to deploy a pod
    - Cloud controller, that is used to for example provision cloud provider's cloud load balancers
- Manifest = yaml file


## Pods
<img src=./possible_pod_states.png width=400>

- Deployable units in k8s
- Ephemeral: they come and go (die) very often
- Scaling an application = add more pods
- Pods host containers. Usually one pod = one container, but for some special cases (eg. when an app needs a support/helper app) one pod can have multiple containers. Containers within one pod can talk to each other via `localhost`, can share volumes and RAM
- One pod can only live on one node
- All containers in the same pod have the same IP address
- Pod is in READY state, when all its containers are up and running (atomicity -> pod is either ready or no, no in-between states)
- Pods run `kubelet`, a process that registers the pod with the cluster, communicates with API and watches the API for new tasks
- Pod states:
    - PENDING: pod is scheduled to a node and waits for all its containers to be ready
    - RUNNING: after all pod containers are ready
    - FAILED: when pod containers can't spin up or get broken
    - SUCCEEDED: after pod completed all its tasks
- Pod scheduled via Pod manifest (singleton pod) can't self-heal, that's why we use Deployments




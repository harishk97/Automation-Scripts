while ! minikube status; do
    echo "Waiting for minikube.."
    sleep 5  
done

echo "minikube is now running."

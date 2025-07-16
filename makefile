build:
	cd docker && ./build-and-run.sh

clean:
	cd docker && ./clean.sh

train-dqn:
	docker exec -e PYTHONPATH=/app -it rl-agent python agents/train_dqn.py

train-ppo:
	docker exec -e PYTHONPATH=/app -it rl-agent python agents/train_ppo.py

evaluate:
	docker exec -e PYTHONPATH=/app -it rl-agent python evaluation/evaluate_agents.py

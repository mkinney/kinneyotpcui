.DEFAULT_GOAL := fmt

.PHONY:fmt

run:
	python otp.py

dockerb: # build
	docker build -t mkinney/kinneyotpcui:latest .

dockerr: # run
	docker run -it --rm mkinney/kinneyotpcui

dockerc: # clean
	docker system prune

push: dockerb
	docker push mkinney/kinneyotpcui:latest

FORCE: ;

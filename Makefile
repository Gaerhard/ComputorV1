# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaerhard <gaerhard@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/23 18:01:04 by gaerhard          #+#    #+#              #
#    Updated: 2021/09/23 18:04:19 by gaerhard         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME := computor

install:
	@python3 -m pip install -r requirements.txt
clean:
	@rm -rf __pycache__
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	while (temp && temp->next)
	{
		current = current->next;
		temp = temp->next->next;

		if (current == temp)
			return (1);
	}

	return (0);
}

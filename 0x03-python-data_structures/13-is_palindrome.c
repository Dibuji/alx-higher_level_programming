#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *a1 = *head;
	listint_t *a2 = *head;
	int len = 0, i, mid;

	while (a1)
	{
		a1 = a1->next;
		len++;
	}
	if (len % 2 != 0)
	{
		mid = (len / 2) + 1;

		a1 = *head;
		for (i = 1; i < mid; i++)
		{
			a1 = a1->next;
		}
		while (a1)
		{
			a1 = a1->next;
			for (i = 1; i < mid && a2 != a1; i++)
			{
				a2 = a2->next;
			}
			if (a2 == a1)
				return (1);
		}
	}
	return (0);
}

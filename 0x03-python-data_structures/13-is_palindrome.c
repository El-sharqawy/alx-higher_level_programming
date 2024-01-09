#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: a pointer to pointer of first node of listint_t list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *tmp, *prev = NULL, *half = NULL;
	int iIsPal = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (iIsPal);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		tmp = slow;
		slow = slow->next;
	}
	if (fast)
	{
		half = slow->next;
		slow->next = NULL;
	}
	else
		half = slow;
	while (half)
	{
		tmp = half->next;
		half->next = prev;
		prev = half;
		half = tmp;
	}
	half = prev;
	while(half)
	{
		if (half->n != (*head)->n)
		{
			iIsPal = 0;
			break;
		}
		*head = (*head)->next;
		half = half->next;
	}
	return (iIsPal);
}

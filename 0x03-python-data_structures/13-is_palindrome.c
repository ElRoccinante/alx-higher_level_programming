#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to the head of the listint_t list
 * @n: integer to be added to the listint_t list
 * Return: address of the new element, or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = n;
    new->next = *head;
    *head = new;
    return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the listint_t list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *reversed = NULL, *temp = NULL;

    if (*head == NULL || current->next == NULL)
        return (1);

    // Reversing the linked list
    while (current != NULL)
    {
        add_nodeint(&reversed, current->n);
        current = current->next;
    }
    temp = reversed;

    // Comparing original list with reversed list
    while (*head != NULL)
    {
        if ((*head)->n != temp->n)
        {
            free_listint(reversed);
            return (0);
        }
        *head = (*head)->next;
        temp = temp->next;
    }

    free_listint(reversed);
    return (1);
}

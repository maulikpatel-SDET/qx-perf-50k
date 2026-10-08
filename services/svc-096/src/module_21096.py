"""Service module 21096: business logic, no crypto."""


def calculate_total_21096(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21096():
    return 'module 21096 handles orders and invoices'

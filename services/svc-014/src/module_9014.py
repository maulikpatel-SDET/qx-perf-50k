"""Service module 9014: business logic, no crypto."""


def calculate_total_9014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9014():
    return 'module 9014 handles orders and invoices'

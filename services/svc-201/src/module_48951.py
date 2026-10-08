"""Service module 48951: business logic, no crypto."""


def calculate_total_48951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48951():
    return 'module 48951 handles orders and invoices'

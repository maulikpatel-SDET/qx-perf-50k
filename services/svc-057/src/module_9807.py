"""Service module 9807: business logic, no crypto."""


def calculate_total_9807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9807():
    return 'module 9807 handles orders and invoices'

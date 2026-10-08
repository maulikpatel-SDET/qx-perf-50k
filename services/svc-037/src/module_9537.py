"""Service module 9537: business logic, no crypto."""


def calculate_total_9537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9537():
    return 'module 9537 handles orders and invoices'

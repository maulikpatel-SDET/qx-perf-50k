"""Service module 9445: business logic, no crypto."""


def calculate_total_9445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9445():
    return 'module 9445 handles orders and invoices'

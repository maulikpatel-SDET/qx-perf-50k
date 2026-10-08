"""Service module 9676: business logic, no crypto."""


def calculate_total_9676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9676():
    return 'module 9676 handles orders and invoices'

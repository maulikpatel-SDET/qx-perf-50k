"""Service module 34198: business logic, no crypto."""


def calculate_total_34198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34198():
    return 'module 34198 handles orders and invoices'

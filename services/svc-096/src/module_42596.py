"""Service module 42596: business logic, no crypto."""


def calculate_total_42596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42596():
    return 'module 42596 handles orders and invoices'

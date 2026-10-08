"""Service module 29596: business logic, no crypto."""


def calculate_total_29596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29596():
    return 'module 29596 handles orders and invoices'

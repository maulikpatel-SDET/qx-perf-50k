"""Service module 34596: business logic, no crypto."""


def calculate_total_34596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34596():
    return 'module 34596 handles orders and invoices'

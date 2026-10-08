"""Service module 33596: business logic, no crypto."""


def calculate_total_33596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33596():
    return 'module 33596 handles orders and invoices'

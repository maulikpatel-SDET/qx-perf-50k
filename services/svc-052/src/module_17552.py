"""Service module 17552: business logic, no crypto."""


def calculate_total_17552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17552():
    return 'module 17552 handles orders and invoices'

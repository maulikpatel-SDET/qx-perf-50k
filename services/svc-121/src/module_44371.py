"""Service module 44371: business logic, no crypto."""


def calculate_total_44371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44371():
    return 'module 44371 handles orders and invoices'

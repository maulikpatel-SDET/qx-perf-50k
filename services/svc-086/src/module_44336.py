"""Service module 44336: business logic, no crypto."""


def calculate_total_44336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44336():
    return 'module 44336 handles orders and invoices'

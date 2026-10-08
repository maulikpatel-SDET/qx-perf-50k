"""Service module 44968: business logic, no crypto."""


def calculate_total_44968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44968():
    return 'module 44968 handles orders and invoices'

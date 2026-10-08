"""Service module 47189: business logic, no crypto."""


def calculate_total_47189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47189():
    return 'module 47189 handles orders and invoices'

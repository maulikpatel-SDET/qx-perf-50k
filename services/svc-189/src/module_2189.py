"""Service module 2189: business logic, no crypto."""


def calculate_total_2189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2189():
    return 'module 2189 handles orders and invoices'

"""Service module 38984: business logic, no crypto."""


def calculate_total_38984(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38984():
    return 'module 38984 handles orders and invoices'

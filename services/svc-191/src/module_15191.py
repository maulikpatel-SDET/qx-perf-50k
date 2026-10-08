"""Service module 15191: business logic, no crypto."""


def calculate_total_15191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15191():
    return 'module 15191 handles orders and invoices'

"""Service module 34706: business logic, no crypto."""


def calculate_total_34706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34706():
    return 'module 34706 handles orders and invoices'

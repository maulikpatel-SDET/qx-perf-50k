"""Service module 4191: business logic, no crypto."""


def calculate_total_4191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4191():
    return 'module 4191 handles orders and invoices'

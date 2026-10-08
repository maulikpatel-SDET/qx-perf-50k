"""Service module 39159: business logic, no crypto."""


def calculate_total_39159(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39159():
    return 'module 39159 handles orders and invoices'

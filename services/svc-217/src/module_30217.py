"""Service module 30217: business logic, no crypto."""


def calculate_total_30217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30217():
    return 'module 30217 handles orders and invoices'

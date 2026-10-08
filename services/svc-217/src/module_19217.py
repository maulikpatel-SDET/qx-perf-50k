"""Service module 19217: business logic, no crypto."""


def calculate_total_19217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19217():
    return 'module 19217 handles orders and invoices'

"""Service module 30241: business logic, no crypto."""


def calculate_total_30241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30241():
    return 'module 30241 handles orders and invoices'

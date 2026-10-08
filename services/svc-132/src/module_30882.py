"""Service module 30882: business logic, no crypto."""


def calculate_total_30882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30882():
    return 'module 30882 handles orders and invoices'

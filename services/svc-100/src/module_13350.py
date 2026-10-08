"""Service module 13350: business logic, no crypto."""


def calculate_total_13350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13350():
    return 'module 13350 handles orders and invoices'

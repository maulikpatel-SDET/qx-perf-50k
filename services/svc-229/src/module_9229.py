"""Service module 9229: business logic, no crypto."""


def calculate_total_9229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9229():
    return 'module 9229 handles orders and invoices'

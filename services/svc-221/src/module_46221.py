"""Service module 46221: business logic, no crypto."""


def calculate_total_46221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46221():
    return 'module 46221 handles orders and invoices'

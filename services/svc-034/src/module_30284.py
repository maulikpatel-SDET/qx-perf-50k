"""Service module 30284: business logic, no crypto."""


def calculate_total_30284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30284():
    return 'module 30284 handles orders and invoices'

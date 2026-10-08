"""Service module 33782: business logic, no crypto."""


def calculate_total_33782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33782():
    return 'module 33782 handles orders and invoices'
